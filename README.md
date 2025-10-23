# ☁️ AWS CloudFormation Practice

This project demonstrates **incremental CloudFormation templates** integrating **API Gateway**, **Lambda**, and **DynamoDB**.  
Each version (v0–v7) progressively builds on the previous one, adding new AWS resources and features.

---

## 📂 Folder Overview

```
aws-cloudformation-practice/
├── aws-practice-v0.yml          # Basic RestApi setup
├── aws-practice-v1.yml          # Adds initial Lambda integration
├── aws-practice-v2.yml          # Introduces DynamoDB
├── aws-practice-v3.yml          # Adds API Resource and Methods
├── aws-practice-v4.yml          # Adds Deployment and Stage
├── aws-practice-v5.yml          # Includes permissions & policies
├── aws-practice-v6.yml          # Full integration (Lambda + API + DynamoDB)
├── aws-practice-v7.yml          # Final version with separate Lambda zips and clean functions
│
├── fn-list-card.py
├── fn-list-card.zip
├── fn-register-card.py
├── fn-register-card.zip
├── fn-update-card.py
├── fn-update-card.zip
```

---

## 🧠 Project Context

Each YAML file represents an incremental **CloudFormation stack evolution**.  
For example:
- **v0–v2:** Basic REST API and Lambda setup.
- **v3–v5:** Adds API methods, resources, and IAM roles.
- **v6:** Introduces full CRUD structure.
- **v7:** Final version — fully functional **card management API** (list, register, update).

The `fn-*.py` and `.zip` files simulate your **Lambda scripts** as they would appear in an **S3 scripts bucket**.  
In an actual deployment, you can:
- Upload `.zip` to S3 and reference them in CFN.
- **Or** directly upload the `.zip` when deploying in the AWS Console (CloudFormation → Create Stack → Upload a template file).

> 💡 *If your assessment requires using S3 links, follow that. Otherwise, uploading directly to CloudFormation is faster and simpler.*

---

## ⚠️ Important — Troubleshooting & Stack Recreation

If your deployment fails or you encounter unexpected behavior:

**Do not just re-run the same stack.**

Instead:

1. Go to **CloudFormation → Stacks**  
2. Select your stack (e.g., `card-api-v7`)  
3. Choose **Delete**  
4. Wait until it is **completely deleted**  
5. Then **Create Stack** again  

🧩 **CloudFormation may reuse existing resources** (like IAM roles or Lambda functions), which can cause validation or conflict errors.  
Recreating the stack ensures all resources are freshly provisioned and avoids “resource already exists” issues.

---

## 🚀 Deployment

### Option 1 — Deploy via AWS Console
1. Go to **AWS CloudFormation** → *Create stack (with new resources)*.  
2. Upload your desired `aws-practice-vX.yml` file.  
3. Set parameters (if any), review, and deploy.

### Option 2 — Deploy via AWS CLI
```bash
aws cloudformation create-stack   --stack-name card-api-v7   --template-body file://aws-practice-v7.yml   --capabilities CAPABILITY_IAM
```

---

## 🔥 Thunder Client Testing

After deployment, get your **API Gateway endpoint** from the AWS Console → API Gateway → Stages → `dev`.

Example endpoint:
```
https://abc123xyz.execute-api.ap-southeast-1.amazonaws.com/dev
```

### 1️⃣ List Cards
```
GET https://abc123xyz.execute-api.ap-southeast-1.amazonaws.com/dev/list
```
No request body.

✅ Returns all cards from DynamoDB.

---

### 2️⃣ Register a New Card
```
POST https://abc123xyz.execute-api.ap-southeast-1.amazonaws.com/dev/register
```
**Body (JSON):**
```json
{
  "card_no": "1001",
  "acct_name": "Yvan Aquino"
}
```
✅ Adds a new card with:
- `status: INACTIVE`
- `balance: 0`

---

### 3️⃣ Update Card Status
```
POST https://abc123xyz.execute-api.ap-southeast-1.amazonaws.com/dev/update
```
**Body (JSON):**
```json
{
  "card_no": "1001",
  "status": "ACTIVE"
}
```
✅ Updates only the card’s `status` field using its key (`card_no`).

---

## 🧩 Notes

- DynamoDB table name: `card_account_cfn`
- Lambda function names (example):
  - `fn-list-card`
  - `fn-register-card`
  - `fn-update-card`
- All functions use **boto3** and a **DecimalEncoder** to handle numeric fields cleanly in JSON.

---

## 🧰 Tech Stack

| Component | Service |
|------------|----------|
| Compute | AWS Lambda |
| Database | DynamoDB |
| API Layer | API Gateway |
| Infrastructure | CloudFormation |

---

## Feedback

If you have any feedback/comment/request, please reach out to [aquino.ylt@gmail.com](mailto:aquino.ylt@gmail.com).

**Fuel future updates – buy me a coffee!**

[![BuyMeACoffee](https://raw.githubusercontent.com/pachadotdev/buymeacoffee-badges/main/bmc-orange.svg)](https://buymeacoffee.com/yvanlowellaquino)

### Thank you and God bless!
