## Flask Application Design for Travel Scheduling Booking

### HTML Files

**index.html**
- **Purpose:** Main landing page for users to select their travel options and submit their itinerary.
- **Content:**
    - Header with page title and navigation menu
    - Form for user input, including:
        - Origin and destination locations
        - Travel dates
        - Desired modes of transportation (train, bus, flight, donkey, ferry, bike)
    - Submit button

**results.html**
- **Purpose:** Displays the compiled itinerary based on user input.
- **Content:**
    - Header with page title
    - Itinerary details, including:
        - List of selected transportation options
        - Travel times and costs
        - Booking information (if available)

### Routes

**@app.route("/", methods=["GET", "POST"])**
- **Purpose:** Handles the main page form submission.
- **Functionality:**
    - Collects user input from the index.html form.
    - Validates the input (e.g., checking for valid dates, locations).
    - Queries a travel API to retrieve travel options based on user selections.
    - Redirects the user to the results.html page with the compiled itinerary.

**@app.route("/results")**
- **Purpose:** Displays the compiled itinerary.
- **Functionality:**
    - Receives the itinerary data from the previous route.
    - Renders the results.html page with the itinerary details.