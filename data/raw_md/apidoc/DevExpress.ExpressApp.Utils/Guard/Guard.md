---
uid: DevExpress.ExpressApp.Utils.Guard
name: Guard
type: Class
summary: Represents an argument checker. Exposes members used to validate method parameters.
syntax:
  content: public static class Guard
seealso:
- linkId: DevExpress.ExpressApp.Utils.Guard._members
  altText: Guard Members
---
The main purpose of the **Guard** class is to validate parameters passed into a method. The class "guards" methods from passing invalid parameters into them. Methods exposed by the **Guard** class are designed to throw exceptions if a parameter being checked does not pass validation.

Consider the following sample method:

# [C#](#tab/tabid-csharp)

```csharp
public void MyMethod(object myObject, string message) {
    if(myObject == null) {
        throw new ArgumentNullException();
    }
    if(myObject.GetType() != typeof(MyType)) {
        throw new ArgumentException();
    }
    else {                
        //...custom logic here
        if(!string.IsNullOrEmpty(message)) {
            //...custom logic here
        }                
    }                
}
```
***

Having argument checks throughout the body of the method clutters the code and makes it less readable. Moreover, checking arguments in such a manner is not a good way of declaring business logic. The following code snippet illustrates the same method rewritten using the **Guard** class:

# [C#](#tab/tabid-csharp)

```csharp
public void MyMethod(object myObject, string message) {
    Guard.ArgumentNotNull(myObject, nameof(myObject));
    Guard.ArgumentNotNull(message, nameof(message));
    Guard.TypeArgumentIs(typeof(MyType), myObject.GetType(), nameof(myObject));
    //...custom logic here                
}
```
***

As you can see, after the rewrite, the code became shorter and more readable. Also, by using the **Guard** class in such a manner we express and enforce a data contract. Combined with self-describing names of the **Guard** class' methods, this makes the sample code rather self-documenting.

The following table lists the methods exposed by the **Guard** class:

| Method | Description |
|---|---|
| [Guard.ArgumentNotNull](xref:DevExpress.ExpressApp.Utils.Guard.ArgumentNotNull(System.Object,System.String)) | Ensures that a specific argument is not a null reference. |
| [Guard.ArgumentNotNullOrEmpty](xref:DevExpress.ExpressApp.Utils.Guard.ArgumentNotNullOrEmpty(System.String,System.String)) | Ensures that a specific string argument is not a null reference and is not an empty string. |
| [Guard.CheckObjectFromObjectSpace](xref:DevExpress.ExpressApp.Utils.Guard.CheckObjectFromObjectSpace(DevExpress.ExpressApp.IObjectSpace,System.Object)) | Ensures that a specific object belongs to a particular Object Space. |
| [Guard.CreateArgumentOutOfRangeException](xref:DevExpress.ExpressApp.Utils.Guard.CreateArgumentOutOfRangeException(System.Object,System.String)) | Initializes a new **ArgumentOutOfRangeException** class with the specified argument name and value. |
| [Guard.NotDisposed](xref:DevExpress.ExpressApp.Utils.Guard.NotDisposed(DevExpress.ExpressApp.IDisposableExt,System.String[])) | Ensures that a specific object has not been disposed. |
| [Guard.TypeArgumentIs](xref:DevExpress.ExpressApp.Utils.Guard.TypeArgumentIs(System.Type,System.Type,System.String)) | Ensures that an argument has a specific type. |