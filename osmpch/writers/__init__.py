from . import csv, parquet, postgresql, sqlite


def get_writer(writer, *args, **kwargs):
    """Get an instance of the writer class based on the writer name.

    Args:
        writer (str): Name of the writer to use.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        instance: An instance of the writer class.
    """
    if writer == "csv":
        return csv.CSVWriter(*args, **kwargs)
    elif writer == "parquet":
        return parquet.ParquetWriter(*args, **kwargs)
    elif writer == "postgresql":
        return postgresql.PostgreSQLWriter(*args, **kwargs)
    elif writer == "sqlite":
        return sqlite.SQLiteWriter(*args, **kwargs)
    else:
        raise ValueError(f"Unknown writer {writer}")
