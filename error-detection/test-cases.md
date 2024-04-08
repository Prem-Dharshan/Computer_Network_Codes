## 1D PARITY CHECK

### Test Case 1 (No Error):

**Input:**
- Data to be transmitted: `11001100`
- Parity: Even (0)
- Received Data: `11001100`

**Result:**
- The detected result should indicate "No error."

### Test Case 2 (Error Detected):

**Input:**
- Data to be transmitted: `11001100`
- Parity: Even (0)
- Received Data: `11101100` (Error in the 4th bit)

**Result:**
- The detected result should indicate "Error."

### Test Case 3 (No Error):

**Input:**
- Data to be transmitted: `00110011`
- Parity: Odd (1)
- Received Data: `00110011`

**Result:**
- The detected result should indicate "No error."

### Test Case 4 (Error Detected):

**Input:**
- Data to be transmitted: `00110011`
- Parity: Odd (1)
- Received Data: `00110111` (Error in the 5th bit)

**Result:**
- The detected result should indicate "Error."

## 2D PARITY CHECK 

### Test Case 1 (No Error):

**Input:**
- Data 1: `11001100`
- Data 2: `10101010`
- Parity: Even (0)

**Steps:**
1. Add parity bit to each data.
   - Tx Data 1: `110011000`
   - Tx Data 2: `101010101`
2. Create transmitted data by combining both data with their parity bit.
   - Tx Data: `110011000101010101`
3. Enter the received data with no errors.
   - Rx Data 1: `110011000`
   - Rx Data 2: `101010101`

**Result:**
- The detected result should indicate "No error."

### Test Case 2 (Error Detected):

**Input:**
- Data 1: `11001100`
- Data 2: `10101010`
- Parity: Even (0)

**Steps:**
1. Add parity bit to each data.
   - Tx Data 1: `110011000`
   - Tx Data 2: `101010101`
2. Create transmitted data by combining both data with their parity bit.
   - Tx Data: `110011000101010101`
3. Introduce an error in the received data.
   - Rx Data 1: `110010000` (Error in the 5th bit)
   - Rx Data 2: `101010101`

**Result:**
- The detected result should indicate "Error."

### Test Case 3 (No Error):

**Input:**
- Data 1: `00001111`
- Data 2: `11110000`
- Parity: Odd (1)

**Steps:**
1. Add parity bit to each data.
   - Tx Data 1: `000011111`
   - Tx Data 2: `111100001`
2. Create transmitted data by combining both data with their parity bit.
   - Tx Data: `000011111111000001`
3. Enter the received data with no errors.
   - Rx Data 1: `000011111`
   - Rx Data 2: `111100001`

**Result:**
- The detected result should indicate "No error."

### Test Case 4 (Error Detected):

**Input:**
- Data 1: `00001111`
- Data 2: `11110000`
- Parity: Odd (1)

**Steps:**
1. Add parity bit to each data.
   - Tx Data 1: `000011111`
   - Tx Data 2: `111100001`
2. Create transmitted data by combining both data with their parity bit.
   - Tx Data: `000011111111000001`
3. Introduce an error in the received data.
   - Rx Data 1: `000010111` (Error in the 5th bit)
   - Rx Data 2: `111100001`

**Result:**
- The detected result should indicate "Error."



## CHECKSUM

### Test Case 1 (No Error):

**Input:**
- Data to be transmitted: `11001100`
- k (Packet Size): 2
- Received Data: `11001100`

**Result:**
- The detected result should indicate "No error."

### Test Case 2 (Error Detected):

**Input:**
- Data to be transmitted: `11001100`
- k (Packet Size): 2
- Received Data: `11101100` (Error in the 4th bit)

**Result:**
- The detected result should indicate "Error."

### Test Case 3 (No Error):

**Input:**
- Data to be transmitted: `00110011`
- k (Packet Size): 2
- Received Data: `00110011`

**Result:**
- The detected result should indicate "No error."

### Test Case 4 (Error Detected):

**Input:**
- Data to be transmitted: `00110011`
- k (Packet Size): 2
- Received Data: `00110111` (Error in the 5th bit)

**Result:**
- The detected result should indicate "Error."

## CYCLIC REDUNDANCY CHECK (CRC)

### Test Case 1 (No Error):

**Input:**
- Data to be transmitted: `11001100`
- Polynomial key: `1011`
- Received Data: `110011001101`

**Result:**
- The detected result should indicate "No error."

### Test Case 2 (Error Detected):

**Input:**
- Data to be transmitted: `11001100`
- Polynomial key: `1011`
- Received Data: `111011001101` (Error in the 4th bit)

**Result:**
- The detected result should indicate "Error."

### Test Case 3 (No Error):

**Input:**
- Data to be transmitted: `00110011`
- Polynomial key: `10101`
- Received Data: `001100110100`

**Result:**
- The detected result should indicate "No error."

### Test Case 4 (Error Detected):

**Input:**
- Data to be transmitted: `00110011`
- Polynomial key: `10101`
- Received Data: `001101110100` (Error in the 5th bit)

**Result:**
- The detected result should indicate "Error."

