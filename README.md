# Match Striker

Pull only the best missions, hands free! Match Striker is a SikuliX script which navigates the EVE Online mission agent interface, harvesting desirable missions by continuously declining duds.

## Installation

- Clone this repository
- Download these JAR files to the root directory of the repository
  - [SikiluX JAR](https://raiman.github.io/SikuliX1/sikulix.jar)
  - [Jython JAR](https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.1/jython-standalone-2.7.1.jar)

## Usage

- Open the SikuliX IDE
- Load the eve.sikuli script 
- `Optional` modify the region constants to reflect your window position
- Dock in station, open all your agents in a single stack
- Ensure each conversation has available either "Request Mission" or "Complete Mission" action
- Run script