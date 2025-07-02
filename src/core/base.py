from enum import Enum
from pydantic import BaseModel, ConfigDict

class BaseEnum(Enum):
    """
    Base class for all Enums in the application.
    This class can be extended by other enums to inherit common functionality.
    """
    
    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        """
        Returns a list of tuples containing the enum value and its name.
        """
        return [(item.value, item.name) for item in cls]
    
    @classmethod
    def values(cls):
        """
        Returns a list of all enum values.
        """
        return [item.value for item in cls]
    
    @classmethod
    def keys(cls):
        """
        Returns a list of all enum names.
        """
        return [item.name for item in cls]

class BaseSchema(BaseModel):
    """
    Base schema for all Pydantic models in the application.
    This class can be extended by other schemas to inherit common functionality.
    """
    
    model_config = ConfigDict(
        extra="ignore",  # Disallow extra fields if use forbid
        validate_assignment=True,  # Validate assignments to model fields
        protected_namespaces=(),  # No protected namespaces
        use_enum_values=True,  # Use enum values in serialization
        from_attributes=True,  # Allow model creation from attributes
    )

    def to_dict(self, exclude: list[str] = [], include: dict = {}) -> dict:
        """
        Convert the model to a dictionary.

        Args:
            exclude (list[str]): List of fields to exclude from the dictionary.
            include (dict): Dictionary of fields to include or override in the output.

        Returns:
            dict: A dictionary representation of the model, excluding specified fields and including specified overrides.
        """

        data = self.model_dump(exclude_unset=True)

        if exclude:
            for field in exclude:
                data.pop(field, None)

        if include:
            data.update(include)

        return data
        

