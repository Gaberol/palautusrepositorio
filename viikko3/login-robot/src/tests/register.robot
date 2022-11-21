***Settings***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  gaberol  l3ipalaatikko
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  gaberol  l3ipalaatikko
    Input Register Command
    Input Credentials  gaberol  laatikkol3ipa
    Output Should Contain  User with username gaberol already exists

Register With Too Short Username And Valid Password
    Input Credentials  gg  l3ipalaatikko
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  gaberol  l3ipa
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  gaberol  leipalaatikko
    Output Should Contain  Password can not contain only letters a-z
