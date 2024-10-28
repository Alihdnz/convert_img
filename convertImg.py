import os
from PIL import Image
from datetime import datetime

def convert_directory_jpg_to_webp(input_dir, output_dir):
  
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_subdir = os.path.join(output_dir, f'convertidos_{timestamp}')
    os.makedirs(output_subdir, exist_ok=True)
    
  
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg'):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_subdir, output_filename)
            
          
            with Image.open(input_path) as img:
                img.save(output_path, format='WEBP')
                print(f'Convertido {input_path} para {output_path}')

def main():
    
    input_directory = input("Insira o caminho do diretório de imagens JPG: ").strip()
    
   
    output_directory = input(f"Insira o caminho do diretório de saída (pressione Enter para usar '{input_directory}'): ").strip() or input_directory

   
    convert_directory_jpg_to_webp(input_directory, output_directory)
    print("Conversão concluída!")

if __name__ == "__main__":
    main()
