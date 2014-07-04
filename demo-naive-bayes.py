training_data = [
                    {'age': 'lte30', 'income':'high', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'no'},
                    {'age': 'lte30', 'income':'high', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':'no'},
                    {'age': '31to40', 'income':'high', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'medium', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'low', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'low', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'no'},
                    {'age': '31to40', 'income':'low', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': 'lte30', 'income':'medium', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'no'},
                    {'age': 'lte30', 'income':'low', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'medium', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'lte30', 'income':'medium', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': 'lte30', 'income':'medium', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': '31to40', 'income':'medium', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': '31to40', 'income':'high', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'medium', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':'no'},
                ]

for data in training_data:
    print data
