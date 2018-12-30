ab = {
    'Swaroop': 'swaroop@swaroop3.com',
    'Larry': 'larry@gmail.com',
    'Kriti': 'kritigarg1998@gmail.com',
    'Komal': 'komalmittal2016@gmail.com'
}
print("Swaroop's address is", ab['Swaroop'])
del ab['Larry']
print('There are {} contacts\n'.format(len(ab)))
for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))
ab['Poonam'] = 'poonamgarg@gmail.com'
if 'Poonam' in ab:
    print("Poonam's adddress is ",ab['Poonam'])