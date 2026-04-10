`ProgressBarPropertyEditor` is a read-only Property Editor that displays the progress of an operation. XAF measures and displays the value of the bound property in percentages. It supports integer and floating-point data types: `Int16`, `UInt16`, `Int32`, `UInt32`, `Int64`, `UInt64`, `float`, `double`, `Decimal`.

To customize the Property Editor's display format string, specify @DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat and apply [percent format specifier](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings#percent-format-specifier-p). For example, if DisplayFormat is `{0:P2}`, the value appears as percentage with two digits after the decimal point: 100.00%.

The Property Editor's value ranges from 0 to 100 for integer data types, and 0 to 1 for floating-point data types by default. You can change the default `<:0:>` and `<:1:>` in code.

Use the @DevExpress.ExpressApp.Editors.PropertyEditor.EditMask to specify a mask expression for the `ProgressBarPropertyEditor`'s control.
