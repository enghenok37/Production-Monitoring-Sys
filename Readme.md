# Line Monitoring System

## Project Overview
This project implements a line monitoring system using Python with a graphical user interface (GUI) built using `Tkinter`. The system monitors different production lines, displays fault statuses, and allows tracking of downtime for fault repair.

---

## Features
1. **Fault Monitoring and Display**:
   - Identifies faults in different lines (e.g., Moulding, Mechanic, WareHouse, etc.).
   - Updates the display with fault messages and fault status.

2. **Timers for Fault Duration**:
   - Tracks the duration of faults using custom stopwatches for each line.

3. **MQTT Communication**:
   - Subscribes to topics for real-time fault updates.
   - Sends status updates to an MQTT broker.

4. **Interactive GUI**:
   - Displays fault information and statuses visually.
   - Allows monitoring of up to 70 lines simultaneously.

---

## Requirements

### Python Libraries:
- `tkinter`: For creating the graphical user interface.
- `Pillow (PIL)`: For loading and displaying images.
- `time`: For tracking elapsed time.
- `serial`: For serial communication (commented out in the code).
- `paho.mqtt.client`: For MQTT communication.
- `re`: For parsing and processing messages.

### Hardware:
- MQTT broker (configured with IP `192.168.43.190`).
- (Optional) Serial communication setup for line monitoring.

---

## Code Structure

### 1. **Modules and Initialization**
The required modules are imported, and the initial setup for MQTT and the GUI is configured. Key components include:
- Initializing timers for fault tracking.
- Creating a GUI window with frames and labels for displaying faults and line statuses.

### 2. **Fault Handling Logic**
The `updateTextTimer` function updates the GUI based on the current fault status:
- Activates or deactivates fault timers.
- Updates the background color of labels to indicate fault or fixed status.

### 3. **MQTT Communication**
The MQTT client handles real-time fault data:
- The `on_message` function processes incoming messages and updates the GUI.
- The `send_message` function sends acknowledgments to the MQTT broker.

### 4. **Stopwatch Class**
The `StopWatch` class implements timers for tracking fault durations:
- Provides methods to start and stop timers.
- Updates a `StringVar` to display elapsed time in the GUI.

### 5. **GUI Layout**
- **Top Frame**:
  - Displays the title and company logos.
- **Line Status Frame**:
  - Contains a grid of labels for up to 70 lines, showing their current statuses.
- **Fault Frames**:
  - Displays fault details for up to four simultaneous issues.
  - Shows elapsed time for each fault.

---

## How It Works
1. **Startup**:
   - The application connects to the MQTT broker and subscribes to relevant topics.

2. **Fault Detection**:
   - Fault messages are received via MQTT.
   - The GUI updates the line statuses and fault details.
   - Timers start for active faults and stop when faults are resolved.

3. **User Interface**:
   - Fault statuses are visually represented with labels changing colors (red for faults, green for resolved).
   - Timers track fault durations for better monitoring.

---

## GUI Layout Diagram
```
+--------------------------------------------------+
| Top Frame                                        |
|   [Logo 1] [Title: Line Monitoring System] [Logo 2] |
+--------------------------------------------------+
| Line Status Frame                                |
|   [Line 1] [Line 2] ... [Line 10]               |
|   [Line 11] ...                                 |
+--------------------------------------------------+
| Fault Line Frame                                 |
|   [Fault 1] [Fault 2] [Fault 3] [Fault 4]       |
+--------------------------------------------------+
| Fault Timer Frame                                |
|   [Timer 1] [Timer 2] [Timer 3] [Timer 4]       |
+--------------------------------------------------+
```

---

## MQTT Topics and Messages
- **Subscribed Topic**: `Line1`
- **Messages**:
  - Fault type and status.
  - Examples: `IDMoulding:0` (Fault in Moulding), `IDINPUT:1` (Fault fixed in SuperMarket).

---

## Running the Application
1. Ensure Python and the required libraries are installed.
2. Start an MQTT broker and configure it with IP `192.168.43.190`.
3. Run the Python script:
   ```bash
   python line_monitoring_system.py
   ```
4. Interact with the GUI to monitor line statuses and faults in real-time.

---

## Future Enhancements
- Add logging to record fault durations and resolutions.
- Integrate email or SMS notifications for critical faults.
- Improve the GUI design with dynamic resizing and animations.
