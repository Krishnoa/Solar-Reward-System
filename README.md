# Solar Reward System Wallet 

## 🧑‍💻 How to Use It (Simple Steps)

1. Clone the repo or download ZIP.
2. Open terminal inside the folder.
3. Run `pip install django djangorestframework` (if not installed)
4. Run `python manage.py runserver`
5. Hit the API with Postman or curl. 

---

## ⚙️ Tech Stack Used

* **Python 3** 🐍
* **Django** – for building the backend framework
* **Django REST Framework** – for creating REST APIs
* **In-Memory Data** – no database used, just lists and logic

---

## 🤔 What’s Happening Behind the Scenes (in my words)

So look, this whole thing is a mini project where we don’t use any real DB. Just Python lists that act like tables.

* There are fake users, projects, and subscriptions all inside a `data.py` file.
* When you hit the `/rewards/distribute` endpoint, it looks at how much energy (kWh) a project produced, checks who subscribed to it, and gives them reward credits.
* Those rewards go into their `walletBalance`, which also lives in memory.
* And if you want to see your wallet, just call `/user/<id>/wallet` – it’ll show your current balance and what rewards you got in past.

Clean, simple. No database. No rocket science. 😎

---

## 🧪 API Endpoints

### 1. POST /rewards/distribute

Distributes rewards to users based on their subscription.

#### Request:

```json
{
  "projectId": 1,
  "kWh_generated": 300
}
```

#### Response:

```json
{
  "rewards": [
    {
      "userId": 1,
      "creditsEarned": 225.0,
      "newWalletBalance": 725.0
    }
  ]
}
```

---

### 2. GET /user/\:id/wallet

See wallet balance and past rewards.

#### Example:

GET `/user/1/wallet`

#### Response:

```json
{
  "walletBalance": 725.0,
  "rewardHistory": [
    {
      "userId": 1,
      "creditsEarned": 225.0,
      "kWh_generated": 300
    }
  ]
}
```

---

## 📬 Postman Collection

This project comes with a ready-to-use Postman collection file: `SolarCapital.postman_collection.json`

### 🔧 How to Use It:

1. Open Postman
2. Click **Import** > **Raw Text** or **File Upload**
3. Paste or upload the contents of `SolarCapital.postman_collection.json`
4. You’ll see two endpoints:

   * `Distribute Rewards` (POST)
   * `Get Wallet Balance` (GET)
5. Modify the payload or user ID as needed and test away 🚀

---

##
