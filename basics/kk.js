router.post("/withdraw", [auth], async (req, res, next) => {
    const MAXIMUM_WITHDRAW = process.env.MAXIMUM_WITHDRAW;
    const { amount, account_no, bank } = req.body;
    if (MAXIMUM_WITHDRAW && amount > MAXIMUM_WITHDRAW) {
      return res
        .status(400)
        .send("Maximum withdraw at a time is ", MAXIMUM_WITHDRAW);
    }
  
    //transaction object
    const transaction = {
      user: req.user,
      action_id: "5ff51eacd875c40017e9671c",
      name: `Fund Withdrawal`,
      status: "pending",
      parent_category: "outbound_withdraw",
      type: "debit",
      amount,
      description: `You fund withdrawal of ₦${amount} is been processed for ${account_no}, ${bank}.`,
      images: [{ url: "", public_id: "" }],
    };
    //payment object
    const data = { amount, account_no, bank };
    data.status = "pending";
    data.account_name = "account_name" || "";
    data.user = req.user._id;
    data.transfer_status = "manual";
    data.payment_type = "manual_withdraw";
  
    //starting mongoose transaction
    let session;
    try {
      session = await mongoose.startSession();
      session.startTransaction();
      const user = await User.findById(req.user._id);
      console.log('REQUEST MADE')
      // console.log({ user });
      //validate account number
      const accountValidation = await handleBankAccountVerification(
        account_no,
        bank
      );
      if (accountValidation.status === "error" || !accountValidation.data) {
        return res.status(400).send(accountValidation);
      }
  
      //check if the user has sufficient funds to complete the transaction
      if (user.balance < amount) {
        res.status(404).send({ error: "insufficient balance" });
        await session.abortTransaction();
        session.endSession();
        return;
      }
  
      //create a new transaction document
      const newTransaction = await Transaction.create(transaction);
  
      user.balance -= amount;
      data.balance = user.balance;
      const payment = await Payment.create(data);
  
      await user.save();
  
      await session.commitTransaction();
      session.endSession();
  
      res.status(201).json({
        status: true,
        message: "Transfer successful",
        transaction: newTransaction,
        payment,
        user,
      });
    } catch (err) {
      res.status(500).json({ message: err.message });
      await session.abortTransaction();
      session.endSession();
    }
  });
  
  /** get transaction by id*/
  router.all("/transactions/:id", async (req, res) => {
    const transaction = await Transaction.findById(req.params.id);
    if (!transaction) {
      return res.status(404).send({ message: "transaction not found" });
    }
    res.status(200).send(transaction);
  });
  
  /** get payment by id*/
  router.all("/payment/:id", async (req, res) => {
    const payment = await Payment.findById(req.params.id);
    if (!payment) {
      return res.status(404).send({ message: "payment not found" });
    }
    res.status(200).send(payment);
  });