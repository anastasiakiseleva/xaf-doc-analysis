---
uid: DevExpress.Persistent.Base.EmptyEntriesMode
name: EmptyEntriesMode
type: Enum
summary: Specifies the behavior of the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method, when a format item in the string passed to it corresponds to a property that contains a `null` or empty value.
syntax:
  content: public enum EmptyEntriesMode
seealso:
- linkId: DevExpress.Persistent.Base.ObjectFormatter
---
Consider the following example. In it, we define a new **Contact** persistent object. Then, we define the **FullName1** and **FullName2** string variables that are constructed using the **Contact** object's **LastName** and **FirstName** properties.

# [C#](#tab/tabid-csharp)

```csharp
Contact john = new Contact();
john.LastName = "Doe";
john.FirstName = "John";

string FullName1 = ObjectFormatter.Format(
    "{LastName}, {FirstName}", john, EmptyEntriesMode.Default);
string FullName2 = ObjectFormatter.Format(
    "{LastName}, {FirstName}", john, EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty );

// FullName1 = "Doe, John"
// FullName2 = "Doe, John"
```
***

Since in this code snippet both the **LastName** and **FirstName** properties have non-empty values, the **FullName1** and **FullName2** variables contain the same string - "Doe, John".

Now, we remove the **FirstName** property's initialization.

# [C#](#tab/tabid-csharp)

```csharp
Contact john = new Contact();
john.LastName = "Doe";

string FullName1 = ObjectFormatter.Format(
"{LastName}, {FirstName}", john, EmptyEntriesMode.Default); 
string FullName2 = ObjectFormatter.Format(
"{LastName}, {FirstName}", john, EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty ); 

// FullName1 = "Doe,"
// FullName2 = "Doe"
```
***

The **FullName1** and **FullName2** variables contain different strings. 

The **FullName1** variable was constructed using the [EmptyEntriesMode.Default](xref:DevExpress.Persistent.Base.EmptyEntriesMode.Default) mode. Since the **FirstName** property is not initialized and contains a `null` value, the "{FirstName}" format item was removed from the resulting string. 

The **FullName2** variable was constructed using the [EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty](xref:DevExpress.Persistent.Base.EmptyEntriesMode.RemoveDelimiterWhenEntryIsEmpty) mode. The "{FirstName}" format item was removed from the resulting string. Additionally, the delimiter string that precedes the "{FirstName}" format item was removed. In this instance - the comma character.