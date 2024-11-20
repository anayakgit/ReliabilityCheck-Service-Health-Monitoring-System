import random
import time
from abc import ABC, abstractmethod
from typing import List

#interface to define the check policy
class HealthCheckPolicy(ABC):
    @abstractmethod
    def perform_check(self, service: "Service") -> None:
        pass

#concrete policy for basic health check
class BasicHealthCheckPolicy(HealthCheckPolicy):
    def perform_check(self, service: "Service") -> None:
        service.response_time = random.uniform(0.5, 2.5)  #simulate response time
        if random.choice([True, False]):
            service.status = "Healthy"
        else:
            service.status = "Down"

#concrete policy for advanced health check 
class AdvancedHealthCheckPolicy(HealthCheckPolicy):
    def perform_check(self, service: "Service") -> None:
        service.response_time = random.uniform(1.0, 5.0)  
        #simulating complex check
        if random.choice([True, False]):
            service.status = "Healthy"
        else:
            service.status = "Down"

#base class for any service
class Service(ABC):
    def __init__(self, name: str, check_policy: HealthCheckPolicy):
        self.name = name
        self.status = None
        self.response_time = None
        self.check_policy = check_policy  #composition: service has a check policy

    @abstractmethod
    def check_status(self):
        pass

    def get_status_report(self):
        return f"Service: {self.name}, Status: {self.status}, Response Time: {self.response_time}s"

#webService subclass simulating a health check with an API call
class WebService(Service):
    def __init__(self, name: str, url: str, check_policy: HealthCheckPolicy):
        super().__init__(name, check_policy)
        self.url = url

    def check_status(self):
        self.check_policy.perform_check(self)  # Delegating check to policy
        print(f"Checked WebService: {self.name} ({self.url})")

#databaseService subclass simulating health check of a database
class DatabaseService(Service):
    def __init__(self, name: str, check_policy: HealthCheckPolicy):
        super().__init__(name, check_policy)

    def check_status(self):
        self.check_policy.perform_check(self)  # Delegating check to policy
        print(f"Checked DatabaseService: {self.name}")

#serviceHealthMonitor to monitor multiple services
class ServiceHealthMonitor:
    def __init__(self):
        self.services: List[Service] = []

    def add_service(self, service: Service):
        self.services.append(service)

    def check_all_services(self):
        for service in self.services:
            service.check_status()
            print(service.get_status_report())

#example Usage
if __name__ == "__main__":
    #create health check policies
    basic_health_check = BasicHealthCheckPolicy()
    advanced_health_check = AdvancedHealthCheckPolicy()

    #create service objects with different health check policies
    web_service = WebService("Web API", "https://api.example.com", basic_health_check)
    database_service = DatabaseService("Main Database", advanced_health_check)

    #create health monitor and add services
    monitor = ServiceHealthMonitor()
    monitor.add_service(web_service)
    monitor.add_service(database_service)

    #check the health of all services
    while True:
        monitor.check_all_services()
        time.sleep(30)  #delay for the next check, 30 sec
