class Stack:
    def __init__(self):
        
        self.items = []
    
    def push(self, item):
        
        self.items.append(item)
    
    def pop(self):
        """Menghapus dan mengembalikan elemen teratas"""
        if self.is_empty():
            raise IndexError("Stack kosong")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack kosong")
        return self.items[-1]
    
    def is_empty(self):
        """Mengecek apakah stack kosong"""
        return len(self.items) == 0
    
    def size(self):
        """Mengembalikan jumlah elemen"""
        return len(self.items)

# === TEST CASES ===
if __name__ == "__main__":
    print("=" * 50)
    print("TEST ADT STACK (DASAR)")
    print("=" * 50)
    
    stack = Stack()
    
    # Test 1: Empty stack
    assert stack.is_empty() == True, "GAGAL"
    assert stack.size() == 0, "GAGAL"
    print("✓ Test 1 PASSED: Stack kosong")
    
    # Test 2: Push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3, "GAGAL"
    assert stack.is_empty() == False, "GAGAL"
    print("✓ Test 2 PASSED: Push 3 elemen")
    
    # Test 3: Peek
    assert stack.peek() == 30, "GAGAL"
    assert stack.size() == 3, "GAGAL: Peek tidak boleh menghapus"
    print("✓ Test 3 PASSED: Peek = 30")
    
    # Test 4: Pop
    assert stack.pop() == 30, "GAGAL"
    assert stack.pop() == 20, "GAGAL"
    assert stack.size() == 1, "GAGAL"
    print("✓ Test 4 PASSED: Pop benar")
    
    # Test 5: Pop sampai kosong
    stack.pop()
    assert stack.is_empty() == True, "GAGAL"
    print("✓ Test 5 PASSED: Stack kosong setelah pop semua")
    
    print("=" * 50)
    print("🎉 SEMUA TEST PASSED!")
    print("=" * 50)
