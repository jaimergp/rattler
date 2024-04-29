from __future__ import annotations
from typing import Optional

from rattler.rattler import PyNoArchType


class NoArchType:
    _noarch: PyNoArchType

    def __init__(self, noarch: Optional[str] = None) -> NoArchType:
        if noarch is None:
            self._noarch = PyNoArchType.none()
            self._source = None
        elif noarch == "python":
            self._noarch = PyNoArchType.python()
            self._source = "python"
        elif noarch == "generic":
            self._noarch = PyNoArchType.generic()
            self._source = "generic"
        else:
            raise ValueError(
                "NoArchType constructor received unsupported value "
                f"{noarch} for the `noarch` parameter"
            )

    @classmethod
    def _from_py_no_arch_type(cls, py_no_arch_type: PyNoArchType) -> NoArchType:
        """Construct Rattler NoArchType from FFI PyNoArchType object."""
        no_arch_type = cls.__new__(cls)
        no_arch_type._noarch = py_no_arch_type
        no_arch_type._source = py_no_arch_type
        return no_arch_type

    @property
    def generic(self) -> bool:
        """
        Return whether this NoArchType is 'generic'
        >>> NoArchType('generic').generic
        True
        >>> NoArchType('generic').python
        False
        >>>
        """
        return self._noarch.is_generic

    @property
    def none(self) -> bool:
        """
        Return whether this NoArchType is set
        >>> NoArchType(None).none
        True
        >>> NoArchType(None).python
        False
        >>>
        """
        return self._noarch.is_none

    @property
    def python(self) -> bool:
        """
        Return whether this NoArchType is 'python'
        >>> NoArchType('python').python
        True
        >>> NoArchType('python').generic
        False
        >>>
        """
        return self._noarch.is_python

    def __hash__(self) -> int:
        """
        Computes the hash of this instance.

        Examples
        --------
        ```python
        >>> hash(NoArchType("python")) == hash(NoArchType("python"))
        True
        >>> hash(NoArchType("python")) == hash(NoArchType("generic"))
        False
        >>>
        ```
        """
        return self._noarch.__hash__()

    def __eq__(self, other: object) -> bool:
        """
        Returns True if this instance represents the same NoArchType as `other`.

        Examples
        --------
        ```python
        >>> NoArchType("python") == NoArchType("generic")
        False
        >>> NoArchType("python") == NoArchType("python")
        True
        >>> NoArchType("generic") == NoArchType("generic")
        True
        >>> NoArchType("python") == "python"
        False
        >>>
        ```
        """
        if not isinstance(other, NoArchType):
            return False

        return self._noarch == other._noarch

    def __ne__(self, other: object) -> bool:
        """
        Returns True if this instance does not represents the same NoArchType as `other`.

        Examples
        --------
        ```python
        >>> NoArchType("python") != NoArchType("python")
        False
        >>> NoArchType("python") != "python"
        True
        >>>
        ```
        """
        if not isinstance(other, NoArchType):
            return True

        return self._noarch != other._noarch

    def __repr__(self) -> str:
        """
        Returns a representation of the NoArchType.

        Examples
        --------
        ```python
        >>> p = NoArchType("python")
        >>> p
        NoArchType("python")
        >>>
        ```
        """
        return f'NoArchType("{self._source}")'
