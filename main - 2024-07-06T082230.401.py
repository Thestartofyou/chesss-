import chess
import chess.engine

def analyze_move(fen, move, engine_path):
    # Set up the board position
    board = chess.Board(fen)
    
    # Initialize the engine
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        # Get the evaluation before the move
        info_before = engine.analyse(board, chess.engine.Limit(time=0.1))
        score_before = info_before["score"].relative.score()

        # Make the move
        board.push(chess.Move.from_uci(move))
        
        # Get the evaluation after the move
        info_after = engine.analyse(board, chess.engine.Limit(time=0.1))
        score_after = info_after["score"].relative.score()
        
        # Compare the evaluations
        evaluation_change = score_after - score_before
        
        print(f"Move: {move}")
        print(f"Evaluation before move: {score_before}")
        print(f"Evaluation after move: {score_after}")
        print(f"Change in evaluation: {evaluation_change}")
        
        if evaluation_change > 0:
            print("The move is strong.")
        elif evaluation_change < 0:
            print("The move is weak.")
        else:
            print("The move is neutral.")
        
        return evaluation_change

# Example usage
fen = "rnbqkb1r/pppppppp/8/8/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"  # Position after 1. e4
move = "d7d5"  # Move to be analyzed
engine_path = "/path/to/stockfish/stockfish"  # Path to the Stockfish engine

analyze_move(fen, move, engine_path)
