# ⚡ ChargeHub — EV Charging Management System

ChargeHub is a Django-based Electric Vehicle (EV) Charging Management System designed to make EV charging simple, smart, and convenient.

Users can find nearby charging stations, check charger availability, book charging slots, manage their vehicles, make payments, view charging history, receive notifications, and get AI-powered charging insights.

---

## 🚀 Features

### 👤 User Management
- User registration and login
- User profile management
- Edit profile
- Account settings
- Change password

### ⚡ Charging Stations
- Browse available charging stations
- View station details
- View charger availability
- Charger type and power information
- Charging price per kWh
- Station location with map integration

### 🔌 Charger Booking
- Select charging station
- Select available charger
- Select vehicle
- Choose booking date
- Select start and end time
- Automatic charging duration calculation
- Estimated energy consumption
- Estimated charging cost
- Booking confirmation

### 🚗 Vehicle Management
- Add vehicles
- Edit vehicle details
- View registered vehicles
- Set primary vehicle
- Track battery-related information

### 💳 Payments
- Charging payment page
- Multiple payment methods
- Transaction generation
- Payment status
- Payment history
- Payment success page

### 📋 Booking Management
- View current bookings
- View booking details
- Cancel bookings
- Booking status tracking

### 🔋 Charging History
- View completed charging sessions
- Energy consumption
- Charging cost
- Station and charger information
- Vehicle information

### 🔔 Notifications
- Booking confirmation notifications
- User notifications
- Read/unread notification status

### 🤖 AI Charging Insights
- AI-powered charging insights
- Charging recommendations
- Smart EV charging analysis
- Google Gemini integration

### 🛠️ Admin Panel
- Manage charging stations
- Manage chargers
- Manage users
- Manage vehicles
- Manage bookings
- Manage payments
- Manage notifications
- Manage maintenance records

### 🌙 UI & Experience
- Modern EV-focused dashboard
- Responsive design
- Light/Dark mode
- Interactive charging station map
- EV charging video section
- Bootstrap-based interface

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Bootstrap Icons

### Database
- SQLite (Development)

### AI
- Google Gemini API

### Maps
- Interactive map integration

### Tools
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```text
ChargeHub/
│
├── accounts/
├── ai_assistant/
├── analytics/
├── bookings/
├── charging/
├── config/
├── maintenance/
├── notifications/
├── payments/
├── stations/
├── user_notifications/
├── vehicles/
│
├── static/
│   ├── css/
│   ├── Js/
│   ├── images/
│   └── videos/
│
├── templates/
│
├── media/
│
├── manage.py
├── .gitignore
└── README.md


⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/Ahmedbilal778/ChargeHub.git

2. Navigate to the project
cd ChargeHub

3. Create a virtual environment
python -m venv chargehub_env

4. Activate the virtual environment
Windows
chargehub_env\Scripts\activate

5. Install dependencies
pip install django

If additional dependencies are required:
pip install -r requirements.txt

6. Run migrations
python manage.py migrate

7. Create an admin account
python manage.py createsuperuser

8. Start the development server
python manage.py runserver

Open:
http://127.0.0.1:8000/


🔐 Admin Panel
ChargeHub provides a Django admin panel for managing the system.
Admin URL:
http://127.0.0.1:8000/admin/

Administrators can manage:
- Charging Stations
- Chargers
- Users
- Vehicles
- Bookings
- Payments
- Notifications
- Maintenance

🔄 Booking Flow
User
  ↓
Find Charging Station
  ↓
Select Charger
  ↓
Select Vehicle
  ↓
Choose Date & Time
  ↓
Calculate Estimated Energy & Cost
  ↓
Payment
  ↓
Booking Confirmed
  ↓
Notification
  ↓
Charging History

🤖 AI Charging Insights

ChargeHub integrates AI to provide intelligent charging-related insights.
The AI feature can assist users with:
- Charging recommendations
- Energy insights
- EV charging analysis
- Smart charging suggestions

📍 Charging Station Management
Charging stations contain information such as:
- Station name
- Address
- City
- State
- Latitude
- Longitude
- Opening time
- Closing time
- Active/inactive status

Each station can have multiple chargers with:
- Charger number
- Charger type
- Power capacity
- Price per kWh
- Availability status

🔮 Future Enhancements
- PostgreSQL production database
- Real payment gateway integration
- Real-time charger availability
- Live charging session tracking
- Advanced analytics dashboard
- EV charging notifications
- Mobile application
- Enhanced AI charging recommendations
- Real-time station availability using APIs

👨‍💻 Author
Ahmed Bilal
Computer Science Student | Python & Django Developer
GitHub:
https://github.com/Ahmedbilal778