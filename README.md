##  Run the code

1. In your shell, run:
   ```bash
   make run
   ```
   This will:
   * compile `basic.p4`, and
   * start the pod-topo in Mininet and configure all switches with
   the appropriate P4 program + table entries, and
   * configure all hosts with the commands listed in
   [pod-topo/topology.json](./pod-topo/topology.json)

2. You should now see a Mininet command prompt. Open two terminals for `h1` and
`h2`, respectively:
   ```bash
   mininet> xterm h1 h2
   ```

3. Each host includes a small Python-based messaging client and server. In
`h2`'s xterm, start the server:
   ```bash
   ./receive.py
   ```

4. First we will test without tunneling. In `h1`'s xterm, send a message to
`h2`:
   ```bash
   ./send.py 10.0.2.2 "helloworld" --debug
   ```

5. Type `exit` to leave each xterm and the Mininet command line.
   Then, to stop mininet:
   ```bash
   make stop
   ```
   And to delete all pcaps, build files, and logs:
   ```bash
   make clean
   ```
