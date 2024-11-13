""" Use enclosure to create fields """

def create_field_builder(datasource):
    def get_name(fieldname):
        return '[{}].[{}]'.format(datasource, fieldname)
    return get_name

if __name__ == '__main__':
    db1 = create_field_builder('Coffee Chain')
    print(db1('Sales'))

    db2 = create_field_builder('World')
    print(db2('Food Consumption'))
