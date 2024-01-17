import os
import subprocess
import shutil

from PIL import Image
import os
import datetime


def compress_image(input_path, quality=80):
    """
    :param input_path: 输入图片路径
    :param quality: 压缩质量（0-100）
    """
    try:
        with Image.open(input_path) as img:
            # 将图像转换为RGB模式
            img = img.convert('RGB')
            img.save(input_path, 'JPEG', quality=quality, optimize=True, progressive=True)
    except Exception as e:
        print(f"无法处理 {input_path}: {str(e)}")

def compress_images_in_directory(input_dir, quality=80):
    """
    递归压缩目录中的所有图片并替换原始图片
    :param input_dir: 输入目录
    :param quality: 压缩质量（0-100）
    """
    # 遍历目录中的所有文件和子文件夹
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                compress_image(input_path, quality)

def convert_docx_to_md(docx_file, output_dir):
    md_file = os.path.join(output_dir, os.path.splitext(docx_file)[0] + '.md')
    media_folder = os.path.join(output_dir, os.path.splitext(docx_file)[0] + '_media')

    command = [
        'pandoc',
        docx_file,
        '-t', 'markdown-smart',
        '-o', md_file,
        '--extract-media=' + media_folder
    ]

    subprocess.run(command)
    compress_images_in_directory(media_folder)

def main():
    # 获取当前目录下的所有docx文件
    docx_files = [f for f in os.listdir() if f.endswith('.docx')]

    if not docx_files:
        print("当前目录下没有找到docx文件。")
        return

    # 遍历并转换每个docx文件
    for docx_file in docx_files:
        # 生成.md文件在当前目录下
        convert_docx_to_md(docx_file, '.')


        # 使用docx文件的名字创建对应的输出目录
        output_directory = os.path.splitext(docx_file)[0]
        os.makedirs(output_directory, exist_ok=True)
        # 移动.md文件和相关媒体文件到目标目录
        md_file = os.path.splitext(docx_file)[0] + '.md'
        media_folder = os.path.splitext(docx_file)[0] + '_media'
        
        shutil.move(md_file, os.path.join(output_directory, md_file))
        shutil.move(media_folder, os.path.join(output_directory, media_folder))

if __name__ == "__main__":
    main()
