API Endpoints to Test

1. Menu API
/api/menu/              - List all menu items, create new item
/api/menu/<int:pk>/     - Retrieve, update, or delete a specific menu item

2. Booking API
/api/booking/tables/    - List and create table bookings
/api/booking/tables/<int:pk>/ - Retrieve, update, or delete a booking

3. User Authentication
/auth/users/            - List or create users
/auth/token/login/      - Log in and receive authentication token
/auth/token/logout/     - Log out (invalidate token)

