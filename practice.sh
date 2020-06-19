read -p "enter only numbers: " -r rr
if ! [[ $rr =~ ^[0-9]+$ ]]
    then 
        echo "sorry only integers"
    else
        echo "dumb"
fi


