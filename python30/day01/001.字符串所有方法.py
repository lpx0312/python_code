class str(Sequence[str], _str_base):
    @overload
    def __init__(self, o: object = ...) -> None: ...
    @overload
    def __init__(self, o: bytes, encoding: str = ..., errors: str = ...) -> None: ...

    def capitalize(self) -> str: ...
    if sys.version_info >= (3, 3):
        def casefold(self) -> str: ...
    def center(self, __width: int, __fillchar: str = ...) -> str: ...
    def count(self, x: Text, __start: Optional[int] = ..., __end: Optional[int] = ...) -> int: ...
    def encode(self, encoding: Text = ..., errors: Text = ...) -> bytes: ...
    def endswith(self, suffix: Union[Text, Tuple[Text, ...]], start: Optional[int] = ...,
                 end: Optional[int] = ...) -> bool: ...
    def expandtabs(self, tabsize: int = ...) -> str: ...
    def find(self, sub: Text, __start: Optional[int] = ..., __end: Optional[int] = ...) -> int: ...
    def format(self, *args: object, **kwargs: object) -> str: ...
    def format_map(self, map: _FormatMapMapping) -> str: ...
    def index(self, sub: Text, __start: Optional[int] = ..., __end: Optional[int] = ...) -> int: ...
    def isalnum(self) -> bool: ...
    def isalpha(self) -> bool: ...
    if sys.version_info >= (3, 7):
        def isascii(self) -> bool: ...
    def isdecimal(self) -> bool: ...
    def isdigit(self) -> bool: ...
    def isidentifier(self) -> bool: ...
    def islower(self) -> bool: ...
    def isnumeric(self) -> bool: ...
    def isprintable(self) -> bool: ...
    def isspace(self) -> bool: ...
    def istitle(self) -> bool: ...
    def isupper(self) -> bool: ...
    def join(self, __iterable: Iterable[str]) -> str: ...
    def ljust(self, __width: int, __fillchar: str = ...) -> str: ...
    def lower(self) -> str: ...
    def lstrip(self, __chars: Optional[str] = ...) -> str: ...
    def partition(self, __sep: str) -> Tuple[str, str, str]: ...
    def replace(self, __old: str, __new: str, __count: int = ...) -> str: ...
    if sys.version_info >= (3, 9):
        def removeprefix(self, __prefix: str) -> str: ...
        def removesuffix(self, __suffix: str) -> str: ...
    def rfind(self, sub: Text, __start: Optional[int] = ..., __end: Optional[int] = ...) -> int: ...
    def rindex(self, sub: Text, __start: Optional[int] = ..., __end: Optional[int] = ...) -> int: ...
    def rjust(self, __width: int, __fillchar: str = ...) -> str: ...
    def rpartition(self, __sep: str) -> Tuple[str, str, str]: ...
    def rsplit(self, sep: Optional[str] = ..., maxsplit: int = ...) -> List[str]: ...
    def rstrip(self, __chars: Optional[str] = ...) -> str: ...
    def split(self, sep: Optional[str] = ..., maxsplit: int = ...) -> List[str]: ...
    def splitlines(self, keepends: bool = ...) -> List[str]: ...
    def startswith(self, prefix: Union[Text, Tuple[Text, ...]], start: Optional[int] = ...,
                   end: Optional[int] = ...) -> bool: ...
    def strip(self, __chars: Optional[str] = ...) -> str: ...
    def swapcase(self) -> str: ...
    def title(self) -> str: ...
    def translate(self, __table: Union[Mapping[int, Union[int, str, None]], Sequence[Union[int, str, None]]]) -> str: ...
    def upper(self) -> str: ...
    def zfill(self, __width: int) -> str: ...
    @staticmethod
    @overload
    def maketrans(__x: Union[Dict[int, _T], Dict[str, _T], Dict[Union[str, int], _T]]) -> Dict[int, _T]: ...
    @staticmethod
    @overload
    def maketrans(__x: str, __y: str, __z: Optional[str] = ...) -> Dict[int, Union[int, None]]: ...

    def __add__(self, s: str) -> str: ...
    # Incompatible with Sequence.__contains__
    def __contains__(self, o: Union[str, Text]) -> bool: ...  # type: ignore
    def __eq__(self, x: object) -> bool: ...
    def __ge__(self, x: Text) -> bool: ...
    def __getitem__(self, i: Union[int, slice]) -> str: ...
    def __gt__(self, x: Text) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __le__(self, x: Text) -> bool: ...
    def __len__(self) -> int: ...
    def __lt__(self, x: Text) -> bool: ...
    def __mod__(self, x: Any) -> str: ...
    def __mul__(self, n: int) -> str: ...
    def __ne__(self, x: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, n: int) -> str: ...
    def __str__(self) -> str: ...
    def __getnewargs__(self) -> Tuple[str]: ...
