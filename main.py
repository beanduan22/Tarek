from datasets import load_dataset

# 允许执行远程代码
dataset = load_dataset("livecodebench/code_generation_lite", version_tag="release_v2", trust_remote_code=True)

problems = dataset["test"]

# 保存到 txt 文件
with open("output.txt", "w", encoding="utf-8") as file:
    for problem in problems:
        problem_id = problem.get('question_id', 'Unknown')
        content = problem.get('question_content', 'No content')
        file.write(f"Problem ID: {problem_id}\nContent: {content}\n\n")

print("save in output.txt")
