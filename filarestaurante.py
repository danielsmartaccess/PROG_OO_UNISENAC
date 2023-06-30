import os
import qrcode

class RestaurantQueue:
    def __init__(self):
        self.code_prefix = 'RES'  # Representa Restaurante
        self.current_number = 0
        self.filename = 'codigos.txt'
        self.queue = {}
        self.check_file_exists()

    def check_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass

    def generate_code(self, people_count):
        self.current_number += 1
        code = f'{self.code_prefix}{str(self.current_number).zfill(3)}-{people_count}'
        self.queue[code] = people_count
        self.save_code_to_file(code)
        self.generate_qrcode(code)
        return code

    def remove_code(self, code):
        if code in self.queue:
            del self.queue[code]
            print(f'Grupo {code} removido da fila.')
        else:
            print('Código inválido ou grupo já atendido.')

    def display_queue(self):
        if self.queue:
            print('Fila:')
            for code, people_count in self.queue.items():
                print(f'Código: {code}, Pessoas no grupo: {people_count}')
        else:
            print('A fila está vazia.')

    def save_code_to_file(self, code):
        with open(self.filename, 'a') as f:
            f.write(f'{code}\n')

    def generate_qrcode(self, code):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f'{code} - Just Go')
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'{code}.png')


def main():
    restaurant_queue = RestaurantQueue()

    while True:
        print('Menu:')
        print('1 - Adicionar grupo à fila')
        print('2 - Remover grupo da fila')
        print('3 - Exibir fila')
        print('4 - Sair')
        option = input('Selecione uma opção: ')

        if option == '1':
            people_count = input('Digite o número de pessoas no grupo: ')
            print('Código gerado:', restaurant_queue.generate_code(people_count))
        elif option == '2':
            code = input('Digite o código do grupo a ser removido: ')
            restaurant_queue.remove_code(code)
        elif option == '3':
            restaurant_queue.display_queue()
        elif option == '4':
            break
        else:
            print('Opção inválida.')


if __name__ == '__main__':
    main()
