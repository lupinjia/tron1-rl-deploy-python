# 英文 | [中文](README.md)
# tron1-rl-deploy-python

## 1. Running the Simulation

same as the original [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python)

## 2. Running the Control Algorithm

- Open a Bash terminal.

- Clone the control algorithm code:

  ```bash
  git clone --recurse https://github.com/lupinjia/tron1-rl-deploy-python.git
  ```

- Install the motion control development library (if not already installed):

  - For Linux x86_64 environment:

    ```bash
    pip install tron1-rl-deploy-python/limxsdk-lowlevel/python3/amd64/limxsdk-*-py3-none-any.whl
    ```

  - For Linux aarch64 environment:

    ```bash
    pip install tron1-rl-deploy-python/limxsdk-lowlevel/python3/aarch64/limxsdk-*-py3-none-any.whl
    ```

- Set the robot type:

  - List the available robot types using the Shell command:

    ```bash
    tree -L 1 tron1-rl-deploy-python/controllers/model
    ```

    Example output:

    ```plaintext
    tron1-rl-deploy-python/controllers/model
    ├── PF_P441A
    ├── PF_P441B
    ├── PF_P441C
    ├── PF_P441C2
    ├── PF_TRON1A
    ├── SF_TRON1A
    └── WF_TRON1A
    ```

  - Set the robot model type (using `PF_P441C` as an example; replace with your actual robot type):

    ```bash
    echo 'export ROBOT_TYPE=PF_P441C' >> ~/.bashrc && source ~/.bashrc
    ```

- Run the control algorithm:

  ```bash
  python tron1-rl-deploy-python/main.py
  ```

## 3. Virtual Joystick

- Open a Bash terminal.

- Run the robot-joystick:

  ```bash
  ./tron1-mujoco-sim/robot-joystick/robot-joystick
  ```

## 4. Support for USB joystick

We implement the acquisition of USB joystick data through pygame. You can enable it through `--use_usb_joy` command.


## 4. Demonstration of Results

After starting the simulation, type the following command to start the controller:

```bash
python main.py --type=ee --config=ee.yaml --use_usb_joy
```

The state machine logic is as follows:
1. L1 + Y: damping
2. L1 + B: sit (preparation mode beforce walk)
3. L1 + A: walk

Demo gif:

![](https://github.com/lupinjia/genesis_lr_doc/blob/main/source/_static/images/tron1_pf_ee_demo.gif?raw=true)