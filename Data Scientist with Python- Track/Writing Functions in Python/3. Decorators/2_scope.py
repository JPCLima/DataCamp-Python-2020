# Modifying variables outside local scope
def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done()
        # doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()


done = False
wait_until_done()

print('Work done? {}'.format(done))
