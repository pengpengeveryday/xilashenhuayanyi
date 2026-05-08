import os
import re

def format_md_file(file_path):
    """为md文件添加格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 按行分割
    lines = content.split('\n')
    
    # 过滤掉空行，获取有内容的行
    non_empty_lines = [line for line in lines if line.strip()]
    
    if not non_empty_lines:
        return
    
    # 检查第一行是否已经包含###，如果已处理则跳过
    first_line = non_empty_lines[0].strip()
    if first_line.startswith('###'):
        print(f"已跳过（已处理）: {os.path.basename(file_path)}")
        return
    
    # 第一行作为标题
    title = first_line
    
    # 其余行作为段落
    paragraphs = []
    for line in non_empty_lines[1:]:
        line = line.strip()
        if line:
            paragraphs.append(line)
    
    # 构建新的内容
    new_content = f"### {title}\n\n"
    
    for i, paragraph in enumerate(paragraphs):
        new_content += f"{paragraph}\n\n"
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"已格式化: {os.path.basename(file_path)}")

def main():
    directory = r"D:\android\xilashenhuayanyi"
    
    # 获取所有md文件
    md_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    
    # 按文件名排序（按章节号）
    md_files.sort()
    
    count = 0
    for filename in md_files:
        file_path = os.path.join(directory, filename)
        try:
            format_md_file(file_path)
            count += 1
        except Exception as e:
            print(f"处理失败 {filename}: {e}")
    
    print(f"\n完成！共格式化 {count} 个文件。")

if __name__ == "__main__":
    main()
