Advanced
==============



----------------
Clone and Setup
----------------

If you want to clone the repos (comes with docs and tests), this is what you do:

.. code-block:: shell

    git clone ...
    sudo pip install -r requirements.txt
    sudo python setup.py install

You can run the test cases using nosetests. Do run the test, you need to rename `credentials-sample.py` to `credentials.py`, and enter the required credentials and details.

--------------------
Phone Number Format
--------------------

You would have noticed that all the phone numbers are in full international format eg. with + and country code and area code. However, you can change the behaviour by setting the prefix and achieve the same.

.. code-block:: python

    Hoiio.prefix = '65'
    Hoiio.voice.call('11111111', '22222222')
    # Equivalent to Hoiio.voice.call('+6511111111', '+6522222222')

    # You could mix
    Hoiio.voice.call('+8500000000', '22222222')


