# 这是一个数据统计系统的模板脚本

item_namespaces = [] # 用于存储所有命名空间的名称

def add_namespace(namespace): # 添加一个新的命名空间到列表中
    if namespace not in item_namespaces:
        item_namespaces.append(namespace)
        with open(namespace+'.txt', 'w') as file:
            file.write(f"Title={namespace}\n")
            file.close()
        print(f"命名空间 '{namespace}' 已添加。")
    else:
        print(f"命名空间 '{namespace}' 已存在。")

def list_namespaces(): # 列出所有已添加的命名空间
    if item_namespaces:
        print("当前命名空间列表:")
        for namespace in item_namespaces:
            print(f"- {namespace}")
    else:
        print("没有可用的命名空间。")

def remove_namespace(namespace): # 从列表中移除指定的命名空间
    if namespace in item_namespaces:
        item_namespaces.remove(namespace)
        print(f"命名空间 '{namespace}' 已移除。")
    else:
        print(f"命名空间 '{namespace}' 不存在。")

def main(): # 主函数，提供用户交互
    while True:
        print("\n数据统计系统")
        print("1. 添加命名空间")
        print("2. 列出命名空间")
        print("3. 移除命名空间")
        print("4. 退出")

        choice = input("请选择操作 (1-4): ")

        if choice == '1':
            namespace = input("请输入要添加的命名空间名称: ")
            add_namespace(namespace)
            continue
        elif choice == '2':
            list_namespaces()
            continue
        elif choice == '3':
            namespace = input("请输入要移除的命名空间名称: ")
            remove_namespace(namespace)
            continue
        elif choice == '4':
            print("退出系统。")
            break
        else:
            print("无效的选择，请重试。")

if __name__ == "__main__": # 确保脚本作为主程序运行时执行
    main()