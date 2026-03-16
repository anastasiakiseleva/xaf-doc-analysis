---
uid: "404195"
title: Create a Calculated Property
owner: Anastasiya Kisialeva
---

# Create a Calculated Property

This topic explains how to create calculated properties. 

The example code below declares a `Payment` entity class with the following properties:

* `Rate` (a persistent property)
* `Hours` (a persistent property)
* `Amount` (a [non-persistent](xref:116516), calculated property: `Amount = Rate * Hours`)

> [!NOTE]
> Before you proceed, take a moment to review the previous lesson:
>
> * [](xref:402981)

## Step-by-Step Instructions

1. Navigate to the _MySolution.Module\Business Objects_ folder. Create a `Payment` class. Replace the auto-generated declaration with the following code:

    ```csharp
    using DevExpress.ExpressApp.DC;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;

    [DefaultClassOptions]
    public class Payment : BaseObject {
        public virtual decimal Rate { get; set; }
        public virtual float Hours { get; set; }

        // Use the `PersistentAlias` attribute to specify the property value calculation expression.
        // Call the `EvaluateAlias` method to access the calculated value.
        [PersistentAlias("Rate * Hours")]
        public decimal Amount {
            get { return EvaluateAlias<decimal>(); }
        }
    }
    ```
    [`PersistentAlias`]: xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute
    [`EvaluateAlias`]: xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.EvaluateAlias*

    >[!TIP]
    >
    > You can apply an @DevExpress.Persistent.Base.ImmediatePostDataAttribute to the `Rate` and `Hours` properties. If you do so, any change to these properties immediately forces the `Amount` value to be recalculated.

3. Register the `Payment` type in `DbContext`:

    ```csharp
    public class MySolutionEFCoreDbContext : DbContext {
        //...
        public DbSet<Payment> Payments { get; set; }
    }
    ```

4. Run the application in debug mode with attached debugger. Select the **Payment** item in the navigation control and click **New**. In the Detail View, change the `Rate` and `Hours` properties and note the updated `Amount` value.


    ![|ASP.NET Core Blazor calculable property|](~/images/xaf-calculated-property.gif)

## Next Lesson

[](xref:402157)