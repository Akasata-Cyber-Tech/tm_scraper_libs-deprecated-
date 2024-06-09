def create_and_fill_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating the file: {e}")
    # create_and_fill_file(file_path, file_content)