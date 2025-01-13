flowchart TB
    subgraph Host["Host System"]
        direction TB
        P["Profile Manager"]
        
        subgraph C1["Container 1: Dev Environment"]
            direction TB
            DC1["Chrome Instance"]
            Cookies1["Cookies"]
            Cache1["Cache"]
            Storage1["Local Storage"]
        end
        
        subgraph C2["Container 2: Testing"]
            direction TB
            DC2["Chrome Instance"]
            Cookies2["Cookies"]
            Cache2["Cache"]
            Storage2["Local Storage"]
        end
        
        subgraph C3["Container 3: Production"]
            direction TB
            DC3["Chrome Instance"]
            Cookies3["Cookies"]
            Cache3["Cache"]
            Storage3["Local Storage"]
        end
    end
    
    P --> C1
    P --> C2
    P --> C3
