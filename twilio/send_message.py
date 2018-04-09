from twilio.rest import Client

account_sid = "ACea55e9cf716fdef486d1e61503cc8d0f"
auth_token = "a62805a7a7ed0f9ca9d667d5ff68ba43"
client = Client(account_sid, auth_token)

client.api.account.messages.create(
    body = "Test from laptop",
    to = "+13603370562",
    from_ = "+13602051317")

