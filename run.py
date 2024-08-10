from block_chain import *
from prediction import *

# Create an instance of the Blockchain
my_blockchain = Blockchain()

example_model = "model"
example_data = "/data/mitbih_test.csv"
example_results = make_prediction(model,example_data)

# Add a block to the blockchain
my_blockchain.add_block(example_model, example_data, example_results)

# Print the blockchain
my_blockchain.print_blockchain()