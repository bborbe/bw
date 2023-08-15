# BME280

## dmesg

```
dmesg | grep i2c
```

```
[    6.887408] i2c_dev: i2c /dev entries driver
```

## /boot/config.txt 

```
dtparam=i2c_arm=on,i2c_baudrate=400000
```

## i2cdetect

```
apt-get install i2c-tools libi2c-dev
i2cdetect -y 1
```


## Links

https://pypi.org/project/RPi.bme280/