namespace Program
{
    class App
    {
        static void Main()
        {
            Program.Triple();
        }
    }

    class Program
    {
        public static string [] Triple()
        {
            string [] array = Income();
            string [] triple_array = new string[0];

            for (int i = 0; i < array.Length; i++)
            {
                if (array[i].Length <= 3)
                {
                    triple_array = triple_array.Append(array[i]).ToArray();
                }
            }

            return triple_array;
        }

        public static string [] Income()
        {
            string [] array = new string [0];

            Console.WriteLine("Please, fill in an array: ");
            while (true)
            {
                Console.WriteLine("Enter an element (type 'Space' to break'): ");
                string a = Convert.ToString(Console.ReadLine()!);
                if (a == " ")
                { 
                    break;
                }
                array = array.Append(a).ToArray();
            }
            
            return array;
        }
    }
}