import pywhatkit

# यहाँ अपना सही नंबर डालें (कंट्री कोड +91 के साथ)
target_number = "+919876543210"
my_message = "Hello! Yeh message Python code se automatically aaya hai."

# समय सेट करें (24 घंटे के फॉर्मेट में)
# उदाहरण: अगर अभी रात के 8 बजकर 50 मिनट हो रहे हैं, तो यहाँ 20 और 52 डाल दें (3 मिनट आगे का समय दें)
target_hour = 20
target_minute = 52

print("मैसेज शेड्यूल हो रहा है... कृपया इंतज़ार करें।")

# यह लाइन तय समय पर व्हाट्सऐप वेब खोलेगी और मैसेज भेजेगी
pywhatkit.sendwhatmsg(target_number, my_message, target_hour, target_minute)

print("काम पूरा हुआ! तय समय पर ब्राउज़र अपने आप खुलेगा।")
