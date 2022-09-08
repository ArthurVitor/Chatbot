import funcs, faker

fake = faker.Faker()

for c in range(100):
    funcs.add_client(fake.name(), funcs.gera_numero(), funcs.gera_hora())
