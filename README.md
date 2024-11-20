Description:
This project demonstrates Object-Oriented Programming (OOP) principles by implementing a modular and extensible system for monitoring the health of web services and databases using customizable health-check policies.

Technologies Used:
1. Python
2. Libraries: random, time, abc
   
Key Features:
1. Encapsulation: Each service and health-check policy is encapsulated within dedicated classes.
2. Inheritance: Specialized service types (e.g., WebService, DatabaseService) inherit from a base Service class.
3. Polymorphism: Health-check policies (BasicHealthCheckPolicy and AdvancedHealthCheckPolicy) implement a common HealthCheckPolicy interface for flexible behavior.
4. Composition: Services are composed with specific health-check policies, allowing easy customization.
5. Abstraction: Abstract base classes define the structure and enforce consistent implementation across services and policies.
   
Usage:
1. Clone the repository.
2. Create service instances (e.g., WebService, DatabaseService) with desired health-check policies.
3. Use the ServiceHealthMonitor class to manage and monitor all services.
4. Run the script to check service health periodically and view detailed status reports.
