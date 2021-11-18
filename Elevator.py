class Elevator:
    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime

    def __str__(self) -> str:
        return f"{self._id} , {self._speed} , {self._minFloor} , {self._maxFloor} , {self._closeTime} , {self._openTime} , {self._startTime} , {self._stopTime}"

    def __repr__(self) -> str:
        return f"{self._id} , {self._speed} , {self._minFloor} , {self._maxFloor} , {self._closeTime} , {self._openTime} , {self._startTime} , {self._stopTime}"
