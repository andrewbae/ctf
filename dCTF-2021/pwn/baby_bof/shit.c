unsigned __int64 signin()
{
  int v0; // eax
  size_t v1; // rbx
  int i; // [rsp+4h] [rbp-5Ch]
  __int64 v4[2]; // [rsp+8h] [rbp-58h] BYREF
  __int64 v5; // [rsp+18h] [rbp-48h]
  __int64 v6; // [rsp+20h] [rbp-40h]
  __int64 v7; // [rsp+28h] [rbp-38h]
  char s[24]; // [rsp+30h] [rbp-30h] BYREF
  unsigned __int64 v9; // [rsp+48h] [rbp-18h]

  v9 = __readfsqword(0x28u);
  v4[1] = (__int64)v4;
  puts(
    "Welcome to my super secure login! Ready to enter the password? We also have a nice anti-bot mechanism which asks you"
    " to sum each character!");
  for ( i = 0; i <= 15; ++i )
  {
    v0 = rand() % 256;                          // 0 - 255
    v5 = v0;
    v6 = v0;
    v7 = rand() % 8 + 2;                        // 2 - 9
    printf("Give me the %d secret, summed to %ld!\n", (unsigned int)(i + 1), v7);
    fgets(s, 19, stdin);
    v4[0] = atoi(s);
    v1 = strspn(s, "0123456789");
    if ( v1 != strlen(s) )
      v4[0] = 0LL;
    puts("Your input is: ");
    printf(s, 0LL);
    if ( !v4[0] )
    {
      printf("??????");
      exit(1);
    }
    if ( v6 != v5 )
    {
      printf("Looks like some memory corruption happened. Blame it on cosmic rays but I can't let you in.");
      exit(1);
    }
    if ( v7 + v5 != v4[0] )
    {
      puts("NOPE, GET OUT OF MY SERVER!");
      exit(1);
    }
  }
  win();
  return __readfsqword(0x28u) ^ v9;
}
