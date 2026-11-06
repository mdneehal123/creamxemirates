# Cream X Emirates online store (trycreamxemirates.in)

Static site + 4 Vercel functions. Independent seller store for CXE Glow Restoring Face Crème 30 ml.

## Edit and publish
1. Change prices, domain, WhatsApp number or the online discount at the top of `_build/build.py` (CONFIG).
2. Run `python3 _build/build.py` (writes the pages into the repo root and `api/_packs.json`).
3. Commit and push to `main`; Vercel deploys automatically.

## Vercel environment variables
| Name | What it is |
|---|---|
| `RAZORPAY_KEY_ID` | Razorpay key id (Dashboard > Account & Settings > API keys) |
| `RAZORPAY_KEY_SECRET` | Razorpay key secret |
| `RAZORPAY_WEBHOOK_SECRET` | Secret you type when adding the webhook below |
| `WEB_ORDER_KEY` | Same value as in the GlutaNex Vercel project (sends orders to the Order Desk) |

Razorpay webhook: Dashboard > Webhooks > Add: URL `https://trycreamxemirates.in/api/razorpay-webhook`, event `payment.captured`.

## Order flow
- Pay online: `/api/create-order` → Razorpay checkout → `/api/verify` (and the webhook as backup) → Order Desk as PAID.
- Cash on Delivery: `/api/order` → Order Desk as COD. If saving fails, the customer gets a ready-to-send WhatsApp message.
- Orders land in the Order Desk (skinday.shop) under the brand "Cream X Emirates" (cx).
