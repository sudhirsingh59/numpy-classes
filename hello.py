# import numpy as np
# board = np.zeros((3,3),dtype=int)
# print(board)

# def print_board(b):
#     symbols = {0:" ",1: "x", -1: "o"}
#     for r in range(3):
#         row = " | ".join(symbols[val] for val in b[r])
#         print(" "+ row)
#         if r < 2:
#             print("---+---+---")
#     print()

# def check_winner(b):
#     if 3 in np.sum(b,axis=1) or 3 in np.sum(b,axis=0):
#         return 'x'
#     if -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis=0):
#         return 'o'
#     if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
#         return 'x'
#     if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
#         return "o"
#     if not 0 in b:
#         return 'DRAW'
#     return None

# current = 1
# print("Welcome to Tic tac tow")

# print_board(board)  

# while True:
#     if current == 1:
#         player = 'X'
#     else:
#         player = 'o'

#     try:
#         row = int(input(player + "- Enter row (0,1,2)"))
#         col = int(input(player + "- Enter column (0,1,2)"))

#     except ValueError:
#         print("Plese enter numbers only \n")
#         continue

#     if row < 0 or row > 2 or col < 0 or col > 2:
#         print("row and column must be between 0 and 2")

#     if board[row,col] != 0:
#         print("cell is already taken ")

#     board[row,col] = current
#     print_board(board)

#     result = check_winner(board)

#     if result is not None:
#         if result == "Draw":
#             print("Ohoo its a draw")
#         else:
#             print(result,"wins")
#         break

#     if current == 1:
#         current =-1
#     else:
#         current = 1


import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic Tac Toe", page_icon="❌⭕", layout="centered")

# -------- Game Logic --------
def init_board():
    return np.zeros((3, 3), dtype=int)

def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return 'X'
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return 'O'
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return 'X'
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return 'O'
    if not 0 in b:
        return 'DRAW'
    return None

# -------- Session State --------
if 'board' not in st.session_state:
    st.session_state.board = init_board()
    st.session_state.current = 1
    st.session_state.game_over = False

# -------- UI --------
st.title("🎮 Tic Tac Toe (NumPy + Streamlit)")

player = "X" if st.session_state.current == 1 else "O"
st.subheader(f"Current Player: {player}")

# -------- Board UI --------
for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        val = st.session_state.board[r, c]
        symbol = ""
        if val == 1:
            symbol = "X"
        elif val == -1:
            symbol = "O"

        if cols[c].button(symbol or " ", key=f"{r}-{c}", use_container_width=True, disabled=st.session_state.game_over):
            if st.session_state.board[r, c] == 0 and not st.session_state.game_over:
                st.session_state.board[r, c] = st.session_state.current

                result = check_winner(st.session_state.board)
                if result:
                    st.session_state.game_over = True
                    if result == "DRAW":
                        st.success("😮 It's a Draw!")
                    else:
                        st.success(f"🎉 {result} Wins!")
                else:
                    st.session_state.current *= -1

# -------- Reset Button --------
st.markdown("---")
if st.button("🔄 Restart Game"):
    st.session_state.board = init_board()
    st.session_state.current = 1
    st.session_state.game_over = False
