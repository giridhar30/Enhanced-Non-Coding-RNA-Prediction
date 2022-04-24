import pyfiglet as pfg

print('\n\033[31m' + pfg.figlet_format('E n c R F P', font = 'slant'))
print('Enhanced non coding RNA Family Prediction tool')
print('\033[0m\n\t1 - train the model\n\t2 - test accuracy of the model\n\t3 - predict family of ncRNA sequence\n\t0 - exit\n')
option = int(input('enter your option: '))
print()

def main():
    if option == 0:
        # getting out of the program
        print('\033[31mthank you :D\033[0m\n')
        import sys
        sys.exit()

    elif option == 1:
        # training and saving model
        from model_training import train_model
        from constants import MODEL_NAME
        train_model(MODEL_NAME)

    elif option == 2:
        # testing the accuracy of trained model
        from model_testing import find_accuracy
        accuracy = find_accuracy()
        print('\nAccuracy:\033[31m')
        print("{:.2f}".format(accuracy), end = ' ')
        print('%\033[0m\n')

    elif option == 3:
        # predict family of ncRNA
        from prediction import predict_family
        print('\n\033[31menter the sequence to be classified:')
        sequence = input()
        print('\033[0m')
        if not sequence:
            print('\033[31mempty sequence not allowed\033[0m')
            import sys
            sys.exit()
        family = predict_family(sequence)
        print('\nThe given RNA Sequence belongs to: \n\033[31m' + family + '\033[0m family\n')

    else:
        # invalid option
        print('\033[31minvalid option\033[0m')

if __name__ == '__main__':
    main()
