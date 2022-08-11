from base import bot

r = bot.api.network
for k, v in r.items():
    print(k, v)

print("+" * 20)
nat_type = r.get("nat_type")
if nat_type != "Public":
    print("NAT type:", nat_type)
    print("port:", r.get("addrs"))
