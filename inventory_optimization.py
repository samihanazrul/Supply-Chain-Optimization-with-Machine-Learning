{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "57e3d763-0c29-4ba4-9f43-71959ec41b9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Iimport necessary libraries\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "477e4bce-133e-4035-99cb-4ed1864d566a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Load inventory data\n",
    "inventory_data = pd.read_csv('inventory_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4bf426b5-c975-4b28-b2e4-26f75e2f6cfc",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Inventory Optimization Function\n",
    "def optimize_inventory(inventory_data):\n",
    "    # Identify products that need to be reordered\n",
    "    products_to_reorder = inventory_data[inventory_data['quantity_in_stock'] < inventory_data['reorder_level']]\n",
    "\n",
    "    # Initialize the 'quantity_to_order' column\n",
    "    inventory_data['quantity_to_order'] = 0\n",
    "\n",
    "    # Calculate reorder quantities for products to reorder\n",
    "    inventory_data.loc[products_to_reorder.index, 'quantity_to_order'] = inventory_data['reorder_level'] - inventory_data['quantity_in_stock']\n",
    "\n",
    "    return inventory_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ab0e5fa6-33ed-4941-aea4-2dfe08e003ff",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Apply inventory optimization\n",
    "optimized_inventory = optimize_inventory(inventory_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c439ab33-71eb-4075-b75a-8bdc7021ef02",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Optimized Inventory:\n",
      "   product_id product_name  quantity_in_stock  reorder_level  \\\n",
      "0           1    Product_A                100             30   \n",
      "1           2    Product_B                 80             25   \n",
      "2           3    Product_C                120             40   \n",
      "3           4    Product_D                 60             20   \n",
      "4           5    Product_E                 90             35   \n",
      "5           6    Product_F                110             30   \n",
      "6           7    Product_G                 75             25   \n",
      "7           8    Product_H                 95             40   \n",
      "8           9    Product_I                 70             20   \n",
      "9          10    Product_J                 85             35   \n",
      "\n",
      "   quantity_to_order  \n",
      "0                  0  \n",
      "1                  0  \n",
      "2                  0  \n",
      "3                  0  \n",
      "4                  0  \n",
      "5                  0  \n",
      "6                  0  \n",
      "7                  0  \n",
      "8                  0  \n",
      "9                  0  \n"
     ]
    }
   ],
   "source": [
    "# Display the optimized inventory\n",
    "print(\"Optimized Inventory:\")\n",
    "print(optimized_inventory[['product_id', 'product_name', 'quantity_in_stock', 'reorder_level', 'quantity_to_order']])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
