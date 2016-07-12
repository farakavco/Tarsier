







if __name__ == '__main__':
    data = BookStaticDataService()
    for b in data.get_all():
        print(b)
