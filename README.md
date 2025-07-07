# 🐞 Bug Bounty Challenge: Safe Withdrawal System

Welcome to the **Bug Bounty Challenge**! Your mission is to identify and fix a subtle bug in a simple banking system written in Python.

---

## 💼 Scenario

You're reviewing a `BankAccount` class that allows users to deposit and withdraw money. The class seems fine at first glance, but there's a bug that lets users **withdraw more than they should**.

Your job is to:

1. Find the bug.
2. Fix it.
3. Prove your fix with a test case or clear output.

---

## 🧠 Challenge Objective

### ✅ Requirements:

- Users should **not** be able to withdraw more than their current balance.
- The `withdraw()` method should return `True` if the withdrawal succeeds, otherwise `False`.
- The balance should never go below `0`.

---

## 💻 File: `bank.py`

This script contains:

- A `BankAccount` class with deposit, withdrawal, and balance methods.
- A `simulate()` function to demonstrate its behavior.
- An example where a user starts with `100`, withdraws `50`, then tries to withdraw `60`.

### Example buggy output:
```txt
Initial Balance: 100
Balance after withdrawing 50: 50
Balance after withdrawing 60: -10   ❌ ← This should not happen!
